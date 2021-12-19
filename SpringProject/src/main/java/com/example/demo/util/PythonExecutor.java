package com.example.demo.util;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PythonExecutor {
    public static void main(String[] args){
        String[] inputArgs = new String[2];
        inputArgs[0] = "D:/GitHub/Git/DSproject/FileParserServer/WPWPOI/files/test.docx";
//        inputArgs[0] = "D:/GitHub/Git/DSproject/SpringProject/src/main/resources/test.py";
        inputArgs[1] = "0";
        String s = execute("D:/GitHub/Git/DSproject/FileParserServer/graphParser.py", inputArgs);
        System.out.println(s);
    }

    public static String execute(String scriptPath, String[] args){
        try {
            ProcessBuilder processBuilder = new ProcessBuilder();
            List<String> command = new ArrayList<>();
            command.add("python3");
            command.add(scriptPath);
            Collections.addAll(command, args);
            processBuilder.command(command);
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();
            process.waitFor();
            InputStream inputStream = process.getInputStream();
            InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
            StringBuilder s = new StringBuilder();
            int len = -1;
            char[] c = new char[1024];
            //读取进程输入流中的内容
            while ((len = inputStreamReader.read(c)) != -1) {
                s.append(new String(c, 0, len));
            }
            inputStream.close();
            return s.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
