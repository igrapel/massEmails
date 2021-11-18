package com.company;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;
import java.util.Properties;

public class BitioExample
{
    String sql_statement;
    Connection c;
    String bitApiKey;
    String bitDB;
    String bitUser;
    String bitHost;
    String bitPort;
    Properties props;
    public BitioExample() {
        //"SELECT * FROM \"igrapel/Parents\".\"parents\";"
        //API KEYS
        c = null;
        bitApiKey = "L3zS_SjMWrcphg3R5VHcP7RQ3hXY";
        bitDB = "bitdotio";
        bitUser = "igrapel_demo_db_connection";
        bitHost = "db.bit.io";
        bitPort = "5432"; // We keep this as a string here as we are concact'ing it into the connection string
        props = new Properties();
        props.setProperty("sslmode", "require");
        props.setProperty("user", bitUser);
        props.setProperty("password", bitApiKey);
    }

    /*
        sql_para: SQL String
        dataReturn: True if the query returns information. False if not.
     */
    public void sendSQL(String sql_para, boolean dataReturn)
    {
        sql_statement = sql_para;
        ResultSet rs = null;
        try {
            Class.forName("org.postgresql.Driver");
            c = DriverManager
                    .getConnection("jdbc:postgresql://" + bitHost + ":" + bitPort + "/" + bitDB, props);
            Statement stmt = c.createStatement();
            if(dataReturn)
            {
                rs = stmt.executeQuery(sql_statement);
                while (rs.next()) {
                    ResultSetMetaData rsmd = rs.getMetaData();
                    // The ResultSet .getXXX() methods expect the column index to start at 1.
                    // No idea why.
                    for (int i = 1; i <= rsmd.getColumnCount(); i++) {
                        System.out.print(rsmd.getColumnName(i) + "=" + rs.getString(i) + " ");
                    }
                    System.out.println();
                }
            }
            else{int rowsUpdated = stmt.executeUpdate(sql_statement);}

        } catch (Exception e) {
            e.printStackTrace();
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            System.exit(0);

        }
    }

    public static void main(String args[])
    {
      //BitioExample store = new BitioExample();
      //store.sendSQL("INSERT INTO \"igrapel/Parents\".\"parents\"" +
             // "VALUES ('Julio Leyva', 'leyva.gmail.com', '2021-11-1T22:12:23', 'Failure');", false);
      //store.sendSQL("SELECT * FROM \"igrapel/Parents\".\"parents\";", true);
        //store.sendSQL("DELETE FROM \"igrapel/Parents\".\"parents\" WHERE student = 'Ivan';", false);
    }
}
