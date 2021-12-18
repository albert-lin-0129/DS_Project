package com.example.demo.vo;

import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/12/1 19:25
 * @Description:
 */
@Data
public class ProjectVO {

    String name;

    Integer uid;

    public ProjectVO(){}

    public ProjectVO(String name, Integer uid){
        this.name = name;
        this.uid = uid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getUid() {
        return uid;
    }

    public void setUid(Integer uid) {
        this.uid = uid;
    }
}
