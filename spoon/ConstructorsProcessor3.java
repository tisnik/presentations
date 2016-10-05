import java.util.Set;

import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtConstructor;
import spoon.reflect.cu.SourcePosition;
import spoon.reflect.declaration.ModifierKind;
import spoon.reflect.code.CtStatement;

public class ConstructorsProcessor3 extends AbstractProcessor<CtConstructor> {
    public void process(CtConstructor element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        String name = element.getSimpleName();
        String signature = element.getSignature();

        int statements = element.getBody().getStatements().size();
        int parameters = element.getParameters().size();
        Set<ModifierKind> modifiers = element.getModifiers();

        System.out.println("constructor '" + name + "' with signature '" + signature + "' declared at:" + sp);
        System.out.println("    parameters: " + parameters);
        System.out.println("    statements: " + statements);
        for (ModifierKind modifier : modifiers) {
            System.out.println("    modifier " + modifier);
        }
        System.out.println("    body:");
        for (CtStatement statement: element.getBody().getStatements()) {
            System.out.println("        " +    statement);
        }
        System.out.println();
    }
}

