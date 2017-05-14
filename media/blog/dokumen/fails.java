import java.util.Scanner;

public class fails{
  public fails(){

  }
  public boolean cekPrima(int nilai){
    int validPrima = 0;
    for (int i = 1; i <= nilai ; i++ ) {
      if(nilai%i == 0){
        validPrima++;
      }
    }
    if(validPrima == 2)
      return true;
    else
      return false;
    }
  public static void main(String[] args){
    fails jajal = new fails();
    int a = 0;
    switch (a) {
      case 1:
        a=1;
        default:
          a=2;


    }
    System.out.print(a);
  }
}
