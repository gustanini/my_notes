using System;

namespace FavoriteNumber
{
  class Program
  {
    static void Main(string[] args)
    {
      // Ask user for fave number
      Console.Write("Enter your favorite number!: ");
      // explicit conversion would not work in this case
      //int faveNumber = (int)Console.ReadLine();
      
      // Turn that answer into an int using method
      int faveNumber = Convert.ToInt32(Console.ReadLine());      


    }
  }
}
