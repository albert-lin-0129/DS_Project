package com.example.demo.po;

import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/3/7 14:40
 * @Description:
 */
@Data
public class Relation {

    private Integer rid;

    private Integer pid;

    private String source_id;

    private String target_id;

    private String source;

    private String target;

    private String relation;

    private String type;

    private String hash_id;

    public Relation(String source_id, String target_id, String source, String target,
                    String relation, String hash_id){
        this.source_id = source_id;
        this.target_id = target_id;
        this.source = source;
        this.target = target;
        this.relation = relation;
        this.hash_id = hash_id;
    }

    public Relation(Integer pid, String source_id, String target_id, String source, String target,
                    String relation, String hash_id){
        this.pid = pid;
        this.source_id = source_id;
        this.target_id = target_id;
        this.source = source;
        this.target = target;
        this.relation = relation;
        this.hash_id = hash_id;
    }

    public Relation(){
    }

    public Integer getRid() {
        return rid;
    }

    public void setRid(Integer rid) {
        this.rid = rid;
    }

    public Integer getPid() {
        return pid;
    }

    public void setPid(Integer pid) {
        this.pid = pid;
    }

    public String getSource_id() {
        return source_id;
    }

    public void setSource_id(String source_id) {
        this.source_id = source_id;
    }

    public String getTarget_id() {
        return target_id;
    }

    public void setTarget_id(String target_id) {
        this.target_id = target_id;
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

    public String getHash_id() {
        return hash_id;
    }

    public void setHash_id(String hash_id) {
        this.hash_id = hash_id;
    }
}
