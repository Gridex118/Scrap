public class HelloGUI extends javax.swing.JComponent {

    public static void main(String[] args) {
        javax.swing.JFrame frame = new javax.swing.JFrame("LoL; UwU");
        frame.setSize(300, 300);
        frame.getContentPane().add(new HelloGUI());
        frame.setVisible(true);
    }

    public void paintComponent(java.awt.Graphics graphics) {
        graphics.drawString("Hello, World", 125, 95);
    }
}
