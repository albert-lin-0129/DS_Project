package com.example.demo.vo.Relation;

import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/6/6 23:21
 * @Description:
 */
@Data
public class RData {

    String id;

    String source;

    String target;

    String relation;

    String type;

    public RData(){}

    public RData(String id, String source, String target, String relation, String type){
        this.id = id;
        this.source = source;
        this.target = target;
        this.relation  =relation;
        this.type = type;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }

    public String getRelation() {
        return relation;
    }

    public void setRelation(String relation) {
        this.relation = relation;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}
