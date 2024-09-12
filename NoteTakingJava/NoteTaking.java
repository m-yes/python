import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
* NoteTaking class.
*
* Lets the user take notes.
 */

public class NoteTaking
{
    private static List<String> notes = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args)
    {
        boolean running = true;
        while (running)
        {
            System.out.println("Please select an option: \n");
            System.out.println("1. Enter new note");
            System.out.println("2. Display all notes");
            System.out.println("3. Exit\n");

            int menuOption = scanner.nextInt();
            scanner.nextLine();

            switch (menuOption)
            {
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

    private static void createNewNote()
    {
        System.out.println("Please enter note below: \n");
        String newNote = scanner.nextLine();
        notes.add(newNote);
        System.out.println("Note added." + newNote + "\n");
    }

    private static void displayAllNotes()
    {
        System.out.println("All notes:");
        for (String note : notes)
        {
            System.out.println(note + "\n");
        }
    }
}
