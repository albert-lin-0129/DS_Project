package com.example.demo.po;

import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/11/21 22:16
 * @Description:
 */
@Data
public class Project {

    private Integer id;

    private Integer uid;

    private String name;

    public Project(Integer id, Integer uid, String name){
        this.id = id;
        this.uid = uid;
        this.name = name;
    }

    public Project(Integer uid, String name){
        this.uid = uid;
        this.name = name;
    }

    public Project(){}

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getUid() {
        return uid;
    }

    public void setUid(Integer uid) {
        this.uid = uid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
