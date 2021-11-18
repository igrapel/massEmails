package com.company;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Parent Email: ");
        String destinationEmail = scan.nextLine();
        System.out.println("\nReceived parent email.");
        System.out.println("Student's First Name: ");
        String studentFirstName = scan.nextLine();
        System.out.println("Student's Last Name: ");
        String studentLastName = scan.nextLine();
        String studentName = studentFirstName + " " + studentLastName;
        System.out.println("Male/Female: ");
        String gender = scan.nextLine();
        while(!gender.equalsIgnoreCase("male") && !gender.equalsIgnoreCase("female"))
        {
            System.out.println("Improper gender: Male or Female: ");
            gender = scan.nextLine();
        }
        System.out.println("Nature of Email: ");
        String emailTopic = scan.nextLine();
	    //Email Constructor and send message
        try{
            Email msg = new Email(destinationEmail);
            msg.sendMessage(studentFirstName, gender);
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }

        //Storing Constructor and store
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        LocalDateTime now = LocalDateTime.now();
        String date = dtf.format(now);
        System.out.println(date);
        int indexSpace = date.indexOf(" ");
        String date_bit = date.substring(0,indexSpace) + "T" + date.substring(indexSpace + 1);
        System.out.println(date_bit);
        Storing test = new Storing("igrapel", "gables21");
        test.storeCorrespondense(studentName, destinationEmail, date, emailTopic);

        //bitio
       BitioExample store = new BitioExample();
       store.sendSQL("INSERT INTO \"igrapel/Parents\".\"parents\"" +
                "VALUES ('" + studentName + "', '" + destinationEmail + "', '" + date_bit +
               "', '" + emailTopic + "');", false);
    }
}
