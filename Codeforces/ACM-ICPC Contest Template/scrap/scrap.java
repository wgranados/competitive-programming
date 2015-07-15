import java.awt.Polygon;
import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.io.*;
import java.util.*;


public class main{

	private static BufferedReader br;
	private static StringTokenizer st;
	private static PrintWriter pw;

	/*
	  br = new BufferedReader(new FileReader("scrap-input.txt"));
	  pw = new PrintWriter(new BufferedWriter(new FileWriter("scrap-output.txt")));
	  br = new BufferedReader(new InputStreamReader(System.in));
      pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	  */
	public static void main(String[] args) throws IOException{
		br = new BufferedReader(new FileReader("scrap-input.txt"));
		pw = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

		pw.close();
   }

  //----------------Fast Input------------------
  private static void exitImmediately(){
	  pw.close();
	  System.exit(0);
  }
  private static long readLong() throws IOException{
	  return Long.parseLong(nextToken());
  }
  private static double readDouble() throws IOException{
	  return Double.parseDouble(nextToken());
  }
  private static int readInt() throws IOException{
	  return Integer.parseInt(nextToken());
  }
  private static String nextToken() throws IOException{
	  while(st == null || !st.hasMoreTokens()){
		  if(!br.ready()){
			  exitImmediately();
		  }
		  st = new StringTokenizer(br.readLine().trim());
	  }
	  return st.nextToken();
  }
  //--------------------------------------------------------
}
