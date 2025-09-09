package main;

import java.awt.*;
import javax.swing.*;
import java.io.*;
import java.nio.file.Files;

public class editor {
     public static void main(String args[]) {


        try {
            for (UIManager.LookAndFeelInfo info : UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    UIManager.setLookAndFeel(info.getClassName());
                    break;
                  }
                }
             } catch (Exception e) {
                   e.printStackTrace();
             }  



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

        JTextArea area=new JTextArea();
        JScrollPane scroll=new JScrollPane(area);
        scroll.setBorder(BorderFactory.createTitledBorder("Editor"));
        window.add(scroll, BorderLayout.CENTER);

        JPanel panel=new JPanel(new FlowLayout(FlowLayout.LEFT, 10, 5));
        JButton newFile=new JButton("New File");
        JButton open=new JButton("Open");
        JButton save=new JButton("Save");
        JButton run=new JButton("Run");

        panel.add(newFile);
        panel.add(open);
        panel.add(save);
        panel.add(run);

        window.add(panel, BorderLayout.NORTH);
      
        final File[] currentFile= {null};

        //New File
        newFile.addActionListener(e -> {
            area.setText("");
            currentFile[0]=null;
        });

   
        //Open
        open.addActionListener(e -> {
            JFileChooser chooser=new JFileChooser();
            if(chooser.showOpenDialog(window) == JFileChooser.APPROVE_OPTION) {
                currentFile[0]=chooser.getSelectedFile();
            
                try {
                    String content=new String(java.nio.file.Files.readAllBytes(currentFile[0].toPath())
                    );
                    area.setText(content);
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(window, "Error");
                }
            }
        }); 
           
              
        //Save
        save.addActionListener(e -> {
             JFileChooser fileChooser = new JFileChooser();
    
             if (currentFile[0] != null) {
                fileChooser.setSelectedFile(currentFile[0]);
               }

             if (fileChooser.showSaveDialog(window) == JFileChooser.APPROVE_OPTION) {
                  currentFile[0] = fileChooser.getSelectedFile();

                try (FileWriter writer = new FileWriter(currentFile[0])) {
                      writer.write(area.getText());
                      JOptionPane.showMessageDialog(window, "Saved");
                   } catch (IOException ex) {
                       JOptionPane.showMessageDialog(window, "Error saving file: " + ex.getMessage());
                }
           }
        });
 
        
        //Run
        run.addActionListener(e -> {

            if(currentFile[0] == null){
            JOptionPane.showMessageDialog(window, "Please Insert The Code");
            }
   
            try {
                String f=currentFile[0].getName();
                String a=currentFile[0].getAbsolutePath();

                File file=new File(a);
                String location= file.getParent();

                if (f.endsWith(".java")) {
                   f = f.substring(0, f.length() - 5);
                  }
        
                new ProcessBuilder("cmd", "/c", "start", "cmd", "/k", "cd /d \"" +location+ "\" &&javac *.java && java " +f)
                .start();

             Thread.sleep(500);

             } catch (IOException | InterruptedException ee) {
               ee.printStackTrace();
           }
         });  

         window.setVisible(true);
    }
}






