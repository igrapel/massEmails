package com.company;
import java.io.UnsupportedEncodingException;
import java.util.Properties;
import java.util.Scanner;
import javax.mail.*;
import javax.mail.internet.*;

public class Email {
    Properties props;
    String host;
    String user;
    final String password;
    String to;
    Session session;

    public Email(String to) {

        host = "smtp.office365.com";
        user = "323917@dadeschools.net";//change accordingly
        Scanner inp = new Scanner(System.in);
        System.out.println("Password: ");
        String pw = inp.nextLine();
        password = pw;//change accordingly
        this.to = to;


        //Get the session object
        props = new Properties();
        props.put("mail.smtp.host", host);
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.port", "587");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.ssl.protocols", "TLSv1.2");

        Authenticator auth = new Authenticator()
        {
            @Override
            public PasswordAuthentication getPasswordAuthentication()
            {
                return new PasswordAuthentication(user, password);
            }
        };

        session = Session.getDefaultInstance(props, auth);
    }

    public void sendMessage(String n, String g)
    {
        String gender = g;
        String adj;
        String obj;

        if(gender.equalsIgnoreCase("Male"))
        {
            adj = "his";
            obj = "him";
        }
        else if(gender.equalsIgnoreCase("Female"))
        {
            adj = "her";
            obj = "her";
        }
        else
        {
            adj = "they";
            obj = "their";
        };

        String e_message = "Dear parents, " +
                "\n\nI am " + n + "'s computer science teacher. " + n + " is not completing " + adj + " work. As a result, " +
                n + " is in danger of failing the class. I hope you can speak with " + obj  + " and encourage " + obj +
                " to put in the effort to pass the class." +
                "\n\n" + "Sincerely, \n\nMr. Ilan Grapel\nIB and AP Computer Science \nCoral Gables Senior High";

        //Compose the message
        try {
            MimeMessage message = new MimeMessage(session);
            message.setFrom(new InternetAddress(user, "Coral Gables Senior High: Mr. Ilan Grapel"));
            message.addRecipient(Message.RecipientType.TO,new InternetAddress(to));
            message.setSubject(n + "'s Academic Performance");
            message.setText(e_message);

            //send the message
            Transport.send(message);

            System.out.println("message sent successfully...");

        }
        catch(SendFailedException e)
        {
            System.out.println("Generic error");
            System.exit(1);
        }
        catch (AddressException e)
        {
            System.out.println("Generic error");
            System.exit(1);
        } catch (MessagingException e)
        {
            e.printStackTrace();
        }
        catch (UnsupportedEncodingException e)
        {
            e.printStackTrace();
        }
    }
}
