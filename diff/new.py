"""Tests for API endpoints that performs component search and component analysis."""
import requests

from behave import given, then, when
from urllib.parse import urljoin

from src.parsing import *
from src.utils import *
from src.authorization_tokens import *


@given("Component search service is running")
def running_component_search_api(context):
    """Wait for the component search REST API to be available."""
    if not context.is_component_search_service_running(context):
        context.wait_for_component_search_service(context, 60)


def component_analysis_url(context, ecosystem, component, version):
    """Construct URL for the component analyses REST API call."""
    return urljoin(
        context.coreapi_url,
        "api/v1/component-analyses/{e}/{c}/{v}".format(
            e=ecosystem, c=component, v=version
        ),
    )


def perform_component_search(context, component, use_token):
    """Call API endpoint to search for component."""
    path = "api/v1/component-search/{component}".format(component=component)
    url = urljoin(context.coreapi_url, path)
    if use_token:
        context.response = requests.get(url, headers=authorization(context))
    else:
        context.response = requests.get(url)


@when("I search for component {component} without authorization token")
def search_for_component_without_token(context, component):
    """Search for given component via the component search REST API call."""
    perform_component_search(context, component, False)


@when("I search for component {component} with authorization token")
def search_for_component_with_token(context, component):
    """Search for given component via the component search REST API call."""
    perform_component_search(context, component, True)


@when("I read {ecosystem}/{component}/{version} component analysis")
@when(
    "I read {ecosystem}/{component}/{version} component analysis "
    "{token} authorization token"
)
def read_analysis_for_component(
    context, ecosystem, component, version, token="without"
):
    """Read component analysis (or an error message) for the selected ecosystem."""
    url = component_analysis_url(context, ecosystem, component, version)

    use_token = parse_token_clause(token)

    if use_token:
        context.response = requests.get(url, headers=authorization(context))
    else:
        context.response = requests.get(url)


@when("I start analysis for component {ecosystem}/{component}/{version}")
def start_analysis_for_component(context, ecosystem, component, version):
    """Start the component analysis.

    Start the analysis for given component and version in selected ecosystem.
    Current API implementation returns just two HTTP codes:
    200 OK : analysis is already finished
    401 UNAUTHORIZED : missing or inproper authorization token
    404 NOT FOUND : analysis is started or is in progress
    It means that this test step should check if 200 OK is NOT returned.
    """
    url = component_analysis_url(context, ecosystem, component, version)

    # first check that the analysis is really new
    response = requests.get(url)

    # remember the response for further test steps
    context.response = response

    if response.status_code == 200:
        raise Exception(
            "Bad state: the analysis for component has been " "finished already"
        )
    elif response.status_code not in (401, 404):
        raise Exception(
            "Improper response: expected HTTP status code 401 or 404, "
            "received {c}".format(c=response.status_code)
        )


@when("I wait for {ecosystem}/{component}/{version} component analysis to finish")
@when(
    "I wait for {ecosystem}/{component}/{version} component analysis to finish "
    "{token} authorization token"
)
def finish_analysis_for_component(
    context, ecosystem, component, version, token="without"
):
    """Try to wait for the component analysis to be finished.

    Current API implementation returns just two HTTP codes:
    200 OK : analysis is already finished
    404 NOT FOUND: analysis is started or is in progress
    """
    timeout = context.component_analysis_timeout  # in seconds
    sleep_amount = 10  # we don't have to overload the API with too many calls

    use_token = parse_token_clause(token)

    # three new lines
    # three new lines
    # three new lines

    url = component_analysis_url(context, ecosystem, component, version)

    for _ in range(timeout // sleep_amount):
        if use_token:
            status_code = requests.get(url, headers=authorization(context)).status_code
        else:
            status_code = requests.get(url).status_code
        if status_code == 200:
            break
        elif status_code != 404:
            raise Exception("Bad HTTP status code {c}".format(c=status_code))
        time.sleep(sleep_amount)
    else:
        raise Exception("Timeout waiting for the component analysis results")


@then("I should see {num:d} components ({components}), all from {ecosystem} ecosystem")
def check_components(context, num, components="", ecosystem=""):
    """Check that the specified number of components can be found."""
    components = split_comma_separated_list(components)

    json_data = context.response.json()
    assert json_data is not None

    search_results = json_data["analysis"]
    assert len(search_results) == num
    for search_result in search_results:
        assert search_result["ecosystem"] == ecosystem
        assert search_result["name"] in components


def print_search_results(search_results):
    """Print all components that can be found."""
    print("\n\n\n")
    print("The following components can be found")
    for r in search_results:
        print(r)
    print("\n\n\n")


@then(
    "I should find the analysis for the component {component} from ecosystem {ecosystem}"
)
def check_component_analysis_existence(context, component, ecosystem):
    """Check that the given component can be found in selected ecosystem."""
    json_data = context.response.json()
    search_results = json_data["result"]

    for search_result in search_results:
        if (
            search_result["ecosystem"] == ecosystem
            and search_result["name"] == component
        ):
            return

    # print_search_results(search_results)

    raise Exception(
        "Component {component} for ecosystem {ecosystem} could not be found".format(
            component=component, ecosystem=ecosystem
        )
    )


@then("I should not find the analysis for the {component} from ecosystem {ecosystem}")
def check_component_analysis_nonexistence(context, component, ecosystem):
    """Check that the given component can not be found in the selected ecosystem."""
    json_data = context.response.json()
    search_results = json_data["result"]

    for search_result in search_results:
        if (
            search_result["ecosystem"] == ecosystem
            and search_result["name"] == component
        ):
            raise Exception(
                "Component {component} for ecosystem {ecosystem} was found".format(
                    component=component, ecosystem=ecosystem
                )
            )


@then("I should not find the analysis for the {component} in any ecosystem")
def check_component_analysis_nonexistence(context, component):
    """Check that the given component can not be found in any ecosystem."""
    json_data = context.response.json()
    search_results = json_data["result"]

    for search_result in search_results:
        if search_result["name"] == component:
            ecosystem = search_result["ecosystem"]
            raise Exception(
                "Component {component} for ecosystem {ecosystem} was found".format(
                    component=component, ecosystem=ecosystem
                )
            )
