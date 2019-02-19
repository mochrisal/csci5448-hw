/*
Implementation of an object oriented program that implements creating various Shapes

author: Morgan Allen
cource: csci 5448 Object Oriented Analysis and Design
due date: 2/15/2019
*/

// Parent Shape Class
import java.io.*;
import java.util.*;

class Shape{
    public String name;
    public int sides;
    
    public Shape(String shape_name, int shape_sides){
        name = shape_name;
        sides = shape_sides;
    }

    public void display(){
        System.out.println("This is a method to display a Shape: name = " + name + ", Sides = " + sides);
    }
}

// Circle Class
class Circle extends Shape {
    public Circle(String name){
        super(name, 0);
    }

    public void display(){
        System.out.println("This is a method to display a Circle: name = " + this.name + ", Sides = " + this.sides);
    }
}

// Circle Class
class Triangle extends Shape {
    public Triangle(String name){
        super(name, 3);
    }

    public void display(){
        System.out.println("This is a method to display Triangle: name = " + name + ", Sides = " + sides);
    }
}

// Circle Class
class Square extends Shape {
    public Square(String name){
        super(name, 4);
    }

    public void display(){
        System.out.println("This is a method to display a Square: name = " + name + ", Sides = " + sides);
    }
}

// Main class to test the shapes
class TestShapes{
    public static void main(String[] args){
        Circle c1 = new Circle("c1");
        Circle c2 = new Circle("c2");
        Circle c3 = new Circle("c3");

        Triangle t1 = new Triangle("t1");
        Triangle t2 = new Triangle("t2");
        Triangle t3 = new Triangle("t3");

        Square s1 = new Square("s1");
        Square s2 = new Square("s2");
        Square s3 = new Square("s3");

        ArrayList<Shape> database = new ArrayList<Shape>();
        ArrayList<Shape> circles = new ArrayList<Shape>();
        ArrayList<Shape> triangles = new ArrayList<Shape>();
        ArrayList<Shape> squares = new ArrayList<Shape>();

        // Create the "database" by randomly adding the collection of declared shape objects to a list
        database.add(c1);
        database.add(s2);
        database.add(c3);
        database.add(s1);
        database.add(t2);
        database.add(s3);
        database.add(t3);
        database.add(t1);
        database.add(c2);

        // Sort the database of shapes by type of shape
        System.out.println("Sorting shapes by type...");

        for(Shape sh : database) {
            if (sh instanceof Circle){
                circles.add(sh);
            }
            if (sh instanceof Triangle){
                triangles.add(sh);
            }
            if (sh instanceof Square){
                squares.add(sh);
            }
        }

        //Call the display function for each type of shape
        System.out.println("Circles:");
        for(Shape c : circles){
            c.display();
        }

        System.out.println("Triangles:");
        for(Shape t : triangles){
            t.display();
        }

        System.out.println("Squares:");
        for(Shape s : squares){
            s.display();
        }
    }
}