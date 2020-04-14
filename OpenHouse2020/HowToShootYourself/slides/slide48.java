public static void main(String args[])
{
	String[] list = new String[3];

	int index = 0;

	while ((index < args.length) && ( index < 3 )) {
		list[index++] = args[index];
	}

	for (int i = 0; i < list.length; i++) {
		if (list[i].equals "-help") {
		}
        ...
        ...
        ...
	}	
}
