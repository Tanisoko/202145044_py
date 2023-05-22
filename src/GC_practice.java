public class GC_practice
{
	public static void main(String[] args)
	{
		Person a, b;
		a = new Person("inha");
		b = new Person("inhatc");
		
		b = a; // b가 가리키던 객체는 Garbage가 됨.
		
		System.gc(); // JVM의 판단하에 GC가 일어나지만 해당 메소드를 직접 호출하여 GC를 요청가능.
	}

}
