import java.util.Scanner;

import javax.management.*;
import java.lang.management.ManagementFactory;

public class Main {
   public static void main(String[] args) {
       try {
           String programName = (args.length == 0) ? "foobar" : args[0];

           StatusMBean systemStatus = new Status(programName);

           MBeanServer platformMBeanServer = ManagementFactory.getPlatformMBeanServer();
           ObjectName objectName = new ObjectName("cz.root.app:name=StatusExample");
           platformMBeanServer.registerMBean(systemStatus, objectName);

       } catch (Exception e) {
           e.printStackTrace();
       }

       new Scanner(System.in).nextLine();
   }
}
