package com.example.demo.vo;

import com.example.demo.vo.Entity.EntityVO;
import lombok.Data;

import java.util.List;

@Data
public class GrammarToken {

    List<String> ans;

    List<EntityVO> nodes;

    public GrammarToken(List<String> ans, List<EntityVO> nodes) {
        this.ans = ans;
        this.nodes = nodes;
    }

    public List<String> getAns() {
        return ans;
    }

    public void setAns(List<String> ans) {
        this.ans = ans;
    }

    public List<EntityVO> getNodes() {
        return nodes;
    }

    public void setNodes(List<EntityVO> nodes) {
        this.nodes = nodes;
    }
}

