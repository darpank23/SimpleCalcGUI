import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;






public class CalculatorGUI extends JFrame implements ActionListener {
    private JTextField textField;
    private JButton[] buttons;
    private JPanel panel;

    

    public CalculatorGUI() {
        this.setTitle("Basic Calculator");
        this.setSize(400,400);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);

        panel = new JPanel();
        panel.setBackground(Color.DARK_GRAY);
        panel.setLayout(new GridLayout(4, 4));


        textField = new JTextField();
        textField.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 16));
        textField.setEditable(false);

        buttons = new JButton[16];

        String[] buttonLabels = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        };

        for (int i = 0; i < 16; i++) {
            buttons[i] = new JButton(buttonLabels[i]);
            buttons[i].setFont(new Font(Font.MONOSPACED,Font.PLAIN, 16));
            buttons[i].addActionListener(this);
            panel.add(buttons[i]);
        }

        this.add(textField, BorderLayout.NORTH);
        this.add(panel);
        this.setVisible(true);
    }

    

    @Override
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        if (command.equals("=")) {
            String expression = textField.getText();
            textField.setText(calculateResult(expression));
        } else {
            textField.setText(textField.getText() + command);
        }
    }

    private String calculateResult(String expression) {
        javax.script.ScriptEngineManager manager = new javax.script.ScriptEngineManager();
        javax.script.ScriptEngine engine = manager.getEngineByName("JavaScript");
        try {
            Object result = engine.eval(expression);
            return result.toString();
        } catch (Exception e) {
            return "ERROR";
        }
    }

    public static void main(String[] args) {
        new CalculatorGUI();
    }
}



