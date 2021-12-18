package com.example.demo.vo.Entity;

import lombok.Data;

import java.util.HashMap;

/**
 * @Author: Owen
 * @Date: 2021/6/6 23:16
 * @Description:
 */
@Data
public class EData {

    String name;

    String id;

    String type;

    HashMap<String, Object> property;

    public EData(){}

    public EData(String name, String id, String type, HashMap<String, Object> property){
        this.name = name;
        this.id = id;
        this.type = type;
        this.property = (HashMap<String, Object>) property.clone();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public HashMap<String, Object> getProperty() {
        return property;
    }

    public void setProperty(HashMap<String, Object> property) {
        this.property = property;
    }
}
