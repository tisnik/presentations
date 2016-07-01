TestInstallationGuide = {
    -- required field
    metadata = {
        description = "Check the overal structure of Installation Guide.",
        authors = "Pavel Tisnovsky",
        emails = "ptisnovs@redhat.com",
        changed = "2015-04-23",
        tags = {"Sanity", "XMLcheck", "SmokeTest"},
    },
    -- this demo needs the following tools to be installed on the system:
    requires = {"grep", "xmlstarlet","xmllint"}
}

function TestInstallationGuide.setUp()
    TestInstallationGuide.rootFile = "installation.ditamap"
end

function TestInstallationGuide.tearDown()
    -- good bye
end

function TestInstallationGuide.test1RootFileExistence()
    local filename = TestInstallationGuide.rootFile
    if path.file_exists(filename) then
        pass(filename .. " exists")
    else
        fail(filename .. " does not exist")
    end
end

function TestInstallationGuide.test2Title()
    local filename = TestInstallationGuide.rootFile
    local command = "xmlstarlet sel -t -v '//map/title' " .. filename .. "  2>/dev/null"
    local output = execCaptureOutputAsString(command)

    -- be sure we got *any* output
    is_not_nil(output, filename .. " contains <title> tag")

    -- #output returns string length
    is_true(#output>0, "<title> tag is not empty")

    -- check if title contains given string
    is_true(output:endsWith("Installation"), "<title> tag contains 'Installation'")
end

function TestInstallationGuide.test3Topics()
    local listTopicsCmd = "ls -1 topics/*.dita"
    local topicList = execCaptureOutputAsTable(listTopicsCmd)

    -- be sure we got *any* output
    is_not_nil(topicList, "topic dir exists")

    -- ukazka jak nahradit ternarni operator, zde jednotne/mnozne cislo ;)
    local msg = (#topicList > 1 and 'topics exist' or 'topic exists')
    -- would be nice if at least one topic is found
    is_true(#topicList>0, #topicList .. " " .. msg)

    for _,topicFileName in ipairs(topicList) do
        local command = "xmlstarlet sel -t -v '//topic/@id' " .. topicFileName .. "  2>/dev/null"
        local output = execCaptureOutputAsString(command)

        -- be sure we got *any* output
        is_not_nil(output, topicFileName)

        -- #output returns string length
        is_true(#output>0, "topic ID is set")

    end
end

