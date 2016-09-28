import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtElement;
import spoon.reflect.cu.SourcePosition;

public class ListSourcePositionProcessor extends AbstractProcessor {
    public void process(CtElement element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        System.out.println(position + "\t" + element);
    }
}

