import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'cryptoErase' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING S as parameter.
     */

    public static String cryptoErase(String S) {
        /// TODO
        return "";

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    
        String S = bufferedReader.readLine();

        String result = Result.cryptoErase(S);

        System.out.print(result);
    }
}
