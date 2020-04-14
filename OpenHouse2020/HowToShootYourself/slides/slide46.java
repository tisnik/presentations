public class MyWindowListener extends WindowAdapter {
	// správně mělo být WindowClosed
	public void WindowClose(WindowEvent e) {
		System.exit(0);
	}
}
