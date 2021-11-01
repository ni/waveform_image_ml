import plotly.express as px
import plotly.graph_objects as go
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)
# fig = px.line(x=t, y=np.cos(t), labels={'x':'t', 'y':'cos(t)'})
# fig.show()
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=y))
fig.write_image("images/test.png")