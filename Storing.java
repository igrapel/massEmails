package com.company;
import java.sql.*;
import java.util.Properties;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import java.util.Properties;
import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

public class Storing {
    private String user; //igrapel
    private String password; //gables21
    String url = "jdbc:sqlserver://DESKTOP-TR5JF24\\SQLEXPRESS;databaseName=Contacts";
    
    public Storing(String user, String pw)
    {
        try
        {
            // Step 1: "Load" the JDBC driver
            //Class.forName("com.imaginary.sql.msql.MsqlDriver");
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            // Step 2: Establish the connection to the database
            this.user = user;
            password = pw;

            try {
                Connection conn = DriverManager.getConnection(url, user, password);
            } catch(SQLException e){
                System.out.println("There is an SQL error");
                e.printStackTrace();
            }

        }
        catch (Exception e)
        {
            System.err.println("Got an exception!");
            System.err.println(e.getMessage());
        }
    }

    public void storeCorrespondense(String student, String contact, String date, String comm)
    {
        try{
            Connection conn = DriverManager.getConnection(url,user,password);
            Statement statement = conn.createStatement();
            String SQL_cols = "(Student, email, date_sent, Comment)";
            String SQL_values = "VALUES ('" + student + "', '" + contact + "', '" + date + "', '" + comm + "')";
            String SQL_statement = "INSERT INTO Parents" + SQL_cols +SQL_values;
            System.out.println(SQL_statement);
            statement.executeUpdate(SQL_statement);
        } catch(SQLException e){
            System.out.println("There is an error");
            e.printStackTrace();
        }
    }
    public static void main(String args[]) {
      /** try
        {
            // Step 1: "Load" the JDBC driver
            //Class.forName("com.imaginary.sql.msql.MsqlDriver");
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            // Step 2: Establish the connection to the database
            String url = "jdbc:sqlserver://DESKTOP-TR5JF24\\SQLEXPRESS;databaseName=Contacts";
            String user = "igrapel";
            String password = "gables21";

            try{
                Connection conn = DriverManager.getConnection(url,user,password);
                Statement statement = conn.createStatement();
                String SQL_cols = "(Student, email, date_sent, Comment)";
                String SQL_values = "VALUES ('Maracello Torres', 'RNMT07@HOTMAIL.COM', '2021-10-20', 'Failure Warning')";

                statement.executeUpdate("INSERT INTO Parents" + SQL_cols +SQL_values);
                System.out.println("INSERT INTO Parents" + SQL_cols +SQL_values);
            } catch(SQLException e){
                System.out.println("There is an error");
                e.printStackTrace();
        }

        }
        catch (Exception e)
        {
            System.err.println("D'oh! Got an exception!");
            System.err.println(e.getMessage());
        }
    }**/
        // 2021-11-1T22:12:23
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        LocalDateTime now = LocalDateTime.now();
        String d = dtf.format(now);
        System.out.println(d);
    }
}
