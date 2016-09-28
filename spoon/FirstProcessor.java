import spoon.processing.AbstractProcessor;
import spoon.reflect.declaration.CtElement;

public class FirstProcessor extends AbstractProcessor {
    public void process(CtElement element) {
        System.out.println(element);
    }
}

