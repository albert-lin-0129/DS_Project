package com.example.demo.vo;

import com.example.demo.vo.Entity.EntityVO;
import com.example.demo.vo.Relation.RelationVO;
import lombok.Data;

/**
 * @Author: Owen
 * @Date: 2021/6/6 23:23
 * @Description: Input/Output Knowledge Graph
 */
@Data
public class IOKG {

    EntityVO[] nodes;

    RelationVO[] edges;

    Integer pid;

    public EntityVO[] getNodes() {
        return nodes;
    }

    public void setNodes(EntityVO[] nodes) {
        this.nodes = nodes;
    }

    public RelationVO[] getEdges() {
        return edges;
    }

    public void setEdges(RelationVO[] edges) {
        this.edges = edges;
    }

    public Integer getPid() {
        return pid;
    }

    public void setPid(Integer pid) {
        this.pid = pid;
    }
}
