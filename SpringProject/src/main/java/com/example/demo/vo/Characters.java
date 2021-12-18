package com.example.demo.vo;

import com.alibaba.fastjson.annotation.JSONField;
import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/6/3 14:54
 * @Description:
 */
@Data
public class Characters {

    @JSONField(name = "出生")
    private String birth;

    @JSONField(name = "血统")
    private String blood;

    @JSONField(name = "婚姻状况")
    private String marry;

    @JSONField(name = "物种")
    private String species;

    @JSONField(name = "性别")
    private String gender;

    @JSONField(name = "逝世")
    private String dead;

    @JSONField(name = "头发颜色")
    private String hairColor;

    @JSONField(name = "皮肤颜色")
    private String skinColor;

    @JSONField(name = "眼睛颜色")
    private String eyeColor;

    @JSONField(name = "学院")
    private String college;

    @JSONField(name = "职业")
    private String[] jobs;

    public String getBirth() {
        return birth;
    }

    public void setBirth(String birth) {
        this.birth = birth;
    }

    public String getBlood() {
        return blood;
    }

    public void setBlood(String blood) {
        this.blood = blood;
    }

    public String getMarry() {
        return marry;
    }

    public void setMarry(String marry) {
        this.marry = marry;
    }

    public String getSpecies() {
        return species;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getDead() {
        return dead;
    }

    public void setDead(String dead) {
        this.dead = dead;
    }

    public String getHairColor() {
        return hairColor;
    }

    public void setHairColor(String hairColor) {
        this.hairColor = hairColor;
    }

    public String getSkinColor() {
        return skinColor;
    }

    public void setSkinColor(String skinColor) {
        this.skinColor = skinColor;
    }

    public String getEyeColor() {
        return eyeColor;
    }

    public void setEyeColor(String eyeColor) {
        this.eyeColor = eyeColor;
    }

    public String getCollege() {
        return college;
    }

    public void setCollege(String college) {
        this.college = college;
    }

    public String[] getJobs() {
        return jobs;
    }

    public void setJobs(String[] jobs) {
        this.jobs = jobs;
    }
}
