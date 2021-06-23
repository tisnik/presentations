public interface StatusMBean {
    Integer getAnswer();
    Long getCounter();
    String getProgramName();
    Boolean getSwitchStatus();
    void setSwitchStatus(Boolean newStatus);
    void flipSwitchStatus();
}
