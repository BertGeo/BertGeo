import dgl
import torch
import torch.nn as nn
import torch.nn.functional as F
from dgl.nn.pytorch import SAGEConv

class GraphSage(nn.Module):
    def __init__(self, in_feats, h_feats, num_classes):
        super(GraphSage, self).__init__()
        self.conv1 = SAGEConv(in_feats, h_feats, 'mean')
        self.conv2 = SAGEConv(h_feats, num_classes, 'mean')
        
    def forward(self, graph, features):
        if torch.cuda.is_available():
            device = torch.device('cuda')
        else:
            device = torch.device('cpu')
        h = self.conv1(graph, features.to(device))
        h = F.relu(h)
        h = self.conv2(graph, h)
        return h

# 创建一个图
g = dgl.DGLGraph()
g.add_nodes(5)
g.add_edges([0, 1, 2, 3, 4], [1, 2, 3, 4, 0])

# 定义节点和边的特征
node_feat = torch.randn(5, 10)
edge_feat = torch.randn(5, 5)

# 添加节点和边特征
g.ndata['feat'] = node_feat
g.edata['feat'] = edge_feat

# 定义模型和优化器
model = GraphSage(10, 16, 2)
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
model.to(device)
optimizer = torch.optim.Adam(model.parameters())

# 训练模型
model.train()
n_epochs = 100
for epoch in range(n_epochs):
    logits = model(g, node_feat)
    labels = torch.LongTensor([0, 1, 0, 1, 0]).to(device)
    loss = F.cross_entropy(logits, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch} | Train Loss: {loss.item():.4f}')

# 生成节点向量表征
model.eval()
with torch.no_grad():
    node_embeddings = model(g, node_feat)
    print(node_embeddings.to('cpu'))