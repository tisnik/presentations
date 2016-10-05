import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtConstructor;
import spoon.reflect.reference.CtVariableReference;
import spoon.reflect.cu.SourcePosition;

public class ConstructorsProcessor2 extends AbstractProcessor<CtConstructor> {
    public void process(CtConstructor element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        String name = element.getSimpleName();
        String signature = element.getSignature();

        int statements = element.getBody().getStatements().size();
        int parameters = element.getParameters().size();

        System.out.println("constructor '" + name + "' with signature '" + signature + "' declared at:" + sp);
        System.out.println("    parameters: " + parameters);
        System.out.println("    statements: " + statements);
    }
}

