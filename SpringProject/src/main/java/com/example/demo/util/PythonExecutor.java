package com.example.demo.util;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class PythonExecutor {
    public static void main(String[] args){

    }

    public static String execute(String filePath, String[] args){
        try {
            ProcessBuilder processBuilder = new ProcessBuilder();
            List<String> command = new ArrayList<>();
            command.add("python");
            command.add(filePath);
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
            return null;
        }
    }
}
