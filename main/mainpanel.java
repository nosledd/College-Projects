package main;

import java.util.Scanner;
import java.awt.*;
import javax.swing.*;
import java.io.*;

public class mainpanel {
     public static void main(String args[]) {
        JFrame window=new JFrame();
        ImageIcon icon=new ImageIcon("E:\\test\\mambooo-fotor-bg-remover-20250720205015.png");
        Image image=icon.getImage();


        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window.setResizable(true);              
        window.setMinimumSize(new Dimension(400,300));
        window.setTitle("Yowaimo");
        window.setIconImage(image);
        window.setSize(800, 600);   // initial size
         window.setLocationRelativeTo(null);    // center on screen

       
        JOptionPane.showMessageDialog(window, "This is a Custom Made Notepad to Run Java Programs");

        window.setLayout(new BorderLayout());


       /*  JLabel label = new JLabel("Create File", SwingConstants.CENTER);
        label.setFont(new Font("Arial", Font.BOLD, 20));
        window.add(label, BorderLayout.NORTH); 

         
        JLabel label = new JLabel("Create File");
        label.setFont(new Font("Arial", Font.BOLD, 20));
        label.setAlignmentX(Component.CENTER_ALIGNMENT);
        panel.add(label);


        JPanel panel=new JPanel();
        panel.setLayout(new FlowLayout(FlowLayout.CENTER,10,10));

        JLabel label = new JLabel("Create File");
        label.setFont(new Font("Arial", Font.BOLD, 20));
        label.setAlignmentX(Component.CENTER_ALIGNMENT);
        panel.add(label);


        JTextField text=new JTextField(10);
        panel.add(text);

        JButton button=new JButton("Save");
        panel.add(button);

        window.add(panel,BorderLayout.CENTER);

        window.setVisible(true); */






        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
        panel.setAlignmentX(Component.CENTER_ALIGNMENT);

        JLabel label = new JLabel("Create File");
        label.setFont(new Font("Arial", Font.BOLD, 20));
        label.setAlignmentX(Component.CENTER_ALIGNMENT);
        panel.add(label);

        panel.add(Box.createRigidArea(new Dimension(0, 20))); // spacing

        JTextField text = new JTextField(15);
        text.setMaximumSize(text.getPreferredSize()); // keeps it from stretching
        text.setAlignmentX(Component.CENTER_ALIGNMENT);
        panel.add(text);

        panel.add(Box.createRigidArea(new Dimension(0, 10))); // spacing

        JButton button = new JButton("Save");
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        panel.add(button);

        // Save function
        button.addActionListener(e -> {
            String fileName = text.getText().trim();
            if (!fileName.isEmpty()) {
                try (FileWriter writer = new FileWriter(fileName + ".txt")) {
                    writer.write("This is a new file: " + fileName);
                    JOptionPane.showMessageDialog(window, "File saved successfully!");
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(window, "Error saving file: " + ex.getMessage());
                }
            } else {
                JOptionPane.showMessageDialog(window, "Please enter a file name.");
            }
        });

        //Put the panel in the CENTER of the window
        window.setLayout(new GridBagLayout()); 
        window.add(panel);

        window.setLocationRelativeTo(null);
        window.setVisible(true);

    }
}