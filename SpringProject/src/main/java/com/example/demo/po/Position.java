package com.example.demo.po;

import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/6/7 0:27
 * @Description:
 */
@Data
public class Position {

    private String id;

    private Integer pid;

    private double x;

    private double y;

    public Position(String id, double x, double y){
        this.id = id;
        this.x = x;
        this.y = y;
    }

    public Position(Integer pid, String id, double x, double y){
        this.id = id;
        this.pid = pid;
        this.x = x;
        this.y = y;
    }

    public Position(){}

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Integer getPid() {
        return pid;
    }

    public void setPid(Integer pid) {
        this.pid = pid;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }
}
