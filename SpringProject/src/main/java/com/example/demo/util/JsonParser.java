package com.example.demo.util;

import com.example.demo.dao.PositionMapper;
import com.example.demo.po.Entity;
import com.example.demo.po.Relation;
import com.google.gson.JsonObject;

import com.example.demo.dao.RelationMapper;
import com.example.demo.dao.EntityMapper;
import com.example.demo.dao.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;

import java.io.File;
import java.io.*;
import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Component
public class JsonParser {

    @Autowired
    private static EntityMapper entityMapper;

    @Autowired
    private static RelationMapper relationMapper;

    public static String readJsonFile(String fileName) {
        String jsonStr = "";
        try {
            File jsonFile = new File(fileName);
            FileReader fileReader = new FileReader(jsonFile);
            Reader reader = new InputStreamReader(new FileInputStream(jsonFile),"utf-8");
            int ch = 0;
            StringBuffer sb = new StringBuffer();
            while ((ch = reader.read()) != -1) {
                sb.append((char) ch);
            }
            fileReader.close();
            reader.close();
            jsonStr = sb.toString();
            return jsonStr;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args){
        parseJson("format.json");
    }

    public static void parseJson(String path){

        String s = readJsonFile(path);

        JSONObject jobj = JSON.parseObject(s);

        JSONArray entity_list = jobj.getJSONArray("entity_list");

        JSONArray relation_list = jobj.getJSONArray("relation_list");

        List<Entity> list1 = new ArrayList<>();
        for (int i = 0 ; i < entity_list.size();i++){
            JSONObject key = (JSONObject)entity_list.get(i);
            Entity temp = new Entity();
            temp.setEid(key.get("eid").toString());
            temp.setPid((Integer) key.get("pid"));
            temp.setName(key.get("name").toString());
            temp.setType(key.get("type").toString());
            temp.setProperty(key.get("property").toString());
            list1.add(temp);
        };
        entityMapper.insertEntities(list1);

        List<Relation> list2 = new ArrayList<>();
        for (int i = 0 ; i < relation_list.size();i++){
            JSONObject key = (JSONObject)relation_list.get(i);
            Relation temp = new Relation();
            temp.setRid((Integer) key.get("rid"));
            temp.setHash_id((String) key.get("hash_id"));
            temp.setPid((Integer) key.get("pid"));
            temp.setRelation((String) key.get("relation"));
            temp.setSource((String) key.get("source"));
            temp.setSource_id((String) key.get("source_id"));
            temp.setTarget((String) key.get("target"));
            temp.setTarget_id((String) key.get("target_id"));
            temp.setType((String) key.get("type"));
            list2.add(temp);
        };
        relationMapper.insertRelations(list2);

        return;
    }
}
