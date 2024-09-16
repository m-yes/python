import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * NoteTaking class.
 * Lets the user enter and display notes.
 */
public class NoteTaking {
    private List<String> notes = new ArrayList<>();
    private Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        NoteTaking app = new NoteTaking();
        app.run();
    }

    public void run() {
        boolean running = true;

        while (running) {
            System.out.println("Please select an option: ");
            System.out.println("1. Enter new note");
            System.out.println("2. Display all notes");
            System.out.println("3. Exit");

            int menuOption = getValidMenuOption();

            switch (menuOption) {
                case 1:
                    createNewNote();
                    break;
                case 2:
                    displayAllNotes();
                    break;
                case 3:
                    running = false;
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option, please try again.");
                    break;
            }
        }
    }

    private int getValidMenuOption() {
        int option = -1;
        while (true) {
            try {
                System.out.print("Enter your choice: ");
                option = Integer.parseInt(scanner.nextLine());
                if (option >= 1 && option <= 3) {
                    break;
                } else {
                    System.out.println("Invalid option. Please enter 1, 2, or 3.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }
        return option;
    }

    private void createNewNote() {
        System.out.println("Please enter note below: ");
        String newNote = scanner.nextLine();
        notes.add(newNote);
        System.out.println("Note added: " + newNote + "\n");
    }

    private void displayAllNotes() {
        if (notes.isEmpty()) {
            System.out.println("No notes available.\n");
        } else {
            System.out.println("All notes:");
            for (String note : notes) {
                System.out.println("- " + note);
            }
            System.out.println();
        }
    }
}
