import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		while (T-- > 0) {
		    String s = sc.next();
		    int n = s.length();
		    
		    String left, right;
		    
		    if (n % 2 == 0) {
		        left = s.substring(0, n / 2);
		        right = s.substring(n / 2);
		    } else {
		        left = s.substring(0, n / 2);
		        right = s.substring(n / 2 + 1);
		    }
		    
		    if (isLapindrome(left, right)) {
		        System.out.println("YES");
		    } else {
		        System.out.println("NO");
		    }
		}
	}
	
	static boolean isLapindrome(String a, String b) {
	    int[] count = new int[26];
	    
	    for (char c : a.toCharArray()) {
	        count[c - 'a']++;
	    }
	    
	    for (char c : b.toCharArray()) {
	        count[c - 'a']--;
	    }
	    
	    for (int x : count) {
	        if (x != 0) return false;
	    }
	    
	    return true;
	}
}