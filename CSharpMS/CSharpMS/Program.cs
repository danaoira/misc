// Programmer:  Dana Oira Toribio
// Tutorial:    Getting Started With C# by Microsoft
// Description: A refresher on C# basics since I haven't programmed in C# in 4 years.
// Date:        2016

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharpMS
{
    class Program
    {
        static void Main()
        {
            // Lesson 3
            // Replacing Parts of Strings

            string name = "Dana";
            string greet1 = $"Hello {name}!";
            string greet2 = "Hello " + name + "!";
            string greet3 = String.Format("Hello {0}");
            string greetTemplate = "Hello **NAME**!";
            string greet4 = greetTemplate.Replace("**NAME**", name);
            Console.WriteLine(name);
            Console.WriteLine(greet1);
            Console.WriteLine(greet2);
            Console.WriteLine(greet3);
            Console.WriteLine(greetTemplate);
            Console.WriteLine(greet4);

            Console.Read();
        }
    }
}
