class Biggest
{
public static void main(String args[])
{
int a,b,c;
a=Integer.parseInt(args[0]);
b=Integer.parseInt(args[1]);
c=Integer.parseInt(args[2]);
if ((a>b)&&(a>c))
System.out.println("the largest number is:"+a);
else if(b>c)
System.out.println("the largest number is:"+b);
else
System.out.println("the largest number is:"+c);
}
}