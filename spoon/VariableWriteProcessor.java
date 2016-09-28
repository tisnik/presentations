import spoon.processing.AbstractProcessor;
import spoon.reflect.code.CtVariableWrite;
import spoon.reflect.reference.CtVariableReference;
import spoon.reflect.cu.SourcePosition;

public class VariableWriteProcessor extends AbstractProcessor<CtVariableWrite> {
    public void process(CtVariableWrite element) {
        SourcePosition sp = element.getPosition();
        CtVariableReference variable = element.getVariable();
        String variableName = variable.getSimpleName();
        String position = sp == null ? "unknown" : sp.toString();
        System.out.println("write into variable '" + variableName + "' at " + position);
    }
}

