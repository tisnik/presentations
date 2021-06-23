# Monitoring Apache Kafka

![Kafka logo](images/kafka_logo.png)

## Usage of Kafka

* Message broker on steroids
* Lambda architecture
* Kappa architecture
* Logging platform

![Kafka streams](images/kafka_streams.png)

![Kafka kappa](images/kafka_kappa.png)

## Kafka architecture

* ZooKeeper
* Message brokers

## JMX

* Java Management Extensions
* Standard in Java world for a long time
* Ability to monitor **any** JVM-based application
* Metrics etc. available through *MBeans*
* Standard tool named **jconsole**

(example of **jconsole** usage)

### Simple example of custom MBeans

* MBean definition via interface named `xxxMBean`:

```java
public interface StatusMBean {
    Integer getAnswer();
    String getProgramName();
    Boolean getSwitchStatus();
}
```

* Interface implementation:

```java
public class Status implements StatusMBean {
   private Integer answer;
   private String programName;
   private Boolean switchStatus;

   public Status(String programName) {
       this.answer = 42;
       this.programName = programName;
       this.switchStatus = false;
   }
   
   @Override
   public Integer getAnswer() {
       return this.answer;
   }

   @Override
   public String getProgramName() {
       return this.programName;
   }

   @Override
   public Boolean getSwitchStatus() {
       return switchStatus;
   }
}
```

* MBean export:

```
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
```

(example of **jconsole** usage)

### JMX can be used to *control* applications as well

* MBean definition via interface named `xxxMBean`:

```java
public interface StatusMBean {
    Integer getAnswer();
    Long getCounter();
    String getProgramName();
    Boolean getSwitchStatus();
    void setSwitchStatus(Boolean newStatus);
    void flipSwitchStatus();
}
```

* Interface implementation:

```java
public class Status implements StatusMBean {
   private Integer answer;
   private String programName;
   private Boolean switchStatus;
   private Long counter;

   public Status(String programName) {
       this.answer = 42;
       this.programName = programName;
       this.switchStatus = false;
       this.counter = 0L;
   }
   
   @Override
   public Integer getAnswer() {
       return this.answer;
   }

   @Override
   public Long getCounter() {
       this.counter++;
       return this.counter;
   }

   @Override
   public String getProgramName() {
       return this.programName;
   }

   @Override
   public Boolean getSwitchStatus() {
       return switchStatus;
   }

   @Override
   public void setSwitchStatus(Boolean newStatus) {
       this.switchStatus = newStatus;
   }

   @Override
   public void flipSwitchStatus() {
       System.out.println("Flip switch status called!");
       this.switchStatus = !this.switchStatus;
   }
}
```

* MBean export:

```java
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
```

(example of **jconsole** usage)

## JMX Exporter

* Tool to provide metrics via Prometheus-like HTTP responses
* Used as `agent` for JVM

* Setup

```bash
wget https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/0.15.0/jmx_prometheus_javaagent-0.15.0.jar
touch config.yaml
```
* Usage

```bash
java -javaagent:./jmx_prometheus_javaagent-0.15.0.jar=8080:config.yaml Main
```

* Getting metrics

```bash
curl localhost:8080/metrics
```

### JMX Exporter setup for Kafka broker

```bash
if [ $# -lt 1 ];
then
    echo "USAGE: $0 [-daemon] server.properties [--override property=value]*"
    exit 1
fi
base_dir=$(dirname $0)
 
if [ "x$KAFKA_LOG4J_OPTS" = "x" ]; then
    export KAFKA_LOG4J_OPTS="-Dlog4j.configuration=file:$base_dir/../config/log4j.properties"
fi
 
if [ "x$KAFKA_HEAP_OPTS" = "x" ]; then
    export KAFKA_HEAP_OPTS="-Xmx1G -Xms1G"
fi
 
EXTRA_ARGS=${EXTRA_ARGS-'-name kafkaServer -loggc'}
 
COMMAND=$1
case $COMMAND in
  -daemon)
    EXTRA_ARGS="-daemon "$EXTRA_ARGS
    shift
    ;;
  *)
    ;;
esac
 
export KAFKA_OPTS=' -javaagent:jmx_prometheus_javaagent-0.15.0.jar=9999:./config/kafka-2_0_0.yml'
 
exec $base_dir/kafka-run-class.sh $EXTRA_ARGS kafka.Kafka "$@"
```
