import java.io.*;
import java.util.*;

class Result {

    public static void matrixRotation(List<List<Integer>> matrix, int r) {
        int m = matrix.size();
        int n = matrix.get(0).size();

        int layers = Math.min(m, n) / 2;

        for (int layer = 0; layer < layers; layer++) {

            List<Integer> list = new ArrayList<>();

            // Top row
            for (int j = layer; j < n - layer; j++)
                list.add(matrix.get(layer).get(j));

            // Right column
            for (int i = layer + 1; i < m - layer - 1; i++)
                list.add(matrix.get(i).get(n - layer - 1));

            // Bottom row
            for (int j = n - layer - 1; j >= layer; j--)
                list.add(matrix.get(m - layer - 1).get(j));

            // Left column
            for (int i = m - layer - 2; i > layer; i--)
                list.add(matrix.get(i).get(layer));

            int size = list.size();
            int rot = r % size;

            // Rotate
            List<Integer> rotated = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                rotated.add(list.get((i + rot) % size));
            }

            int idx = 0;

            // Put back

            // Top row
            for (int j = layer; j < n - layer; j++)
                matrix.get(layer).set(j, rotated.get(idx++));

            // Right column
            for (int i = layer + 1; i < m - layer - 1; i++)
                matrix.get(i).set(n - layer - 1, rotated.get(idx++));

            // Bottom row
            for (int j = n - layer - 1; j >= layer; j--)
                matrix.get(m - layer - 1).set(j, rotated.get(idx++));

            // Left column
            for (int i = m - layer - 2; i > layer; i--)
                matrix.get(i).set(layer, rotated.get(idx++));
        }

        // Print result
        for (List<Integer> row : matrix) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] first = br.readLine().split(" ");

        int m = Integer.parseInt(first[0]);
        int n = Integer.parseInt(first[1]);
        int r = Integer.parseInt(first[2]);

        List<List<Integer>> matrix = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            String[] rowInput = br.readLine().split(" ");
            List<Integer> row = new ArrayList<>();

            for (int j = 0; j < n; j++) {
                row.add(Integer.parseInt(rowInput[j]));
            }

            matrix.add(row);
        }

        Result.matrixRotation(matrix, r);
    }
}