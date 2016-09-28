import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtClass;
import spoon.reflect.cu.SourcePosition;

public class ListClassesProcessor extends AbstractProcessor<CtClass> {
    public void process(CtClass element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        System.out.println(position + "\t" + element.getSimpleName());
    }
}

