import java.util.Set;

import spoon.processing.AbstractProcessor;
import spoon.reflect.cu.SourcePosition;
import spoon.reflect.code.CtLoop;
import spoon.reflect.code.CtStatement;

public class LoopDetector extends AbstractProcessor<CtLoop> {
    public void process(CtLoop element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        CtStatement loopStatement = element.getBody();

        System.out.println("loop: " + loopStatement + " declared at:" + sp);
        System.out.println();
    }
}

