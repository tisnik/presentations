import java.util.Set;

import spoon.processing.AbstractProcessor;
import spoon.reflect.cu.SourcePosition;
import spoon.reflect.code.CtWhile;
import spoon.reflect.code.CtStatement;
import spoon.reflect.code.CtExpression;

public class WhileLoopDetector extends AbstractProcessor<CtWhile> {
    public void process(CtWhile element) {
        SourcePosition sp = element.getPosition();
        String position = sp == null ? "unknown" : sp.toString();
        CtStatement loopStatement = element.getBody();
        CtExpression loopingExpression = element.getLoopingExpression();

        System.out.println("loop: " + loopStatement + " declared at:" + sp);
        System.out.println("expression (test): " + loopingExpression);
        System.out.println();
    }
}

