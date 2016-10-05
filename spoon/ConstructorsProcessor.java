import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtConstructor;
import spoon.reflect.cu.SourcePosition;

public class ConstructorsProcessor extends AbstractProcessor<CtConstructor> {
    public void process(CtConstructor element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        String name = element.getSimpleName();
        String signature = element.getSignature();
        System.out.println("constructor '" + name + "' with signature '" + signature + "' declared at:" + sp);
    }
}

