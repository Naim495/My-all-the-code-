import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ✅ Load world boundaries directly from Natural Earth (remote)
world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)

# Extract Bangladesh geometry
bd_geom = world[world["NAME"] == "Bangladesh"].geometry.values[0]

# Convert to list of polygons (handles MultiPolygon too)
if isinstance(bd_geom, Polygon):
    polys = [bd_geom]
elif isinstance(bd_geom, MultiPolygon):
    polys = list(bd_geom.geoms)

# Make 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

for poly in polys:
    x, y = poly.exterior.xy
    verts_bottom = [(xi, yi, 0) for xi, yi in zip(x, y)]
    verts_top    = [(xi, yi, 1) for xi, yi in zip(x, y)]

    ax.add_collection3d(Poly3DCollection([verts_bottom], facecolors="lightgreen", alpha=0.7))
    ax.add_collection3d(Poly3DCollection([verts_top], facecolors="lightgreen", alpha=0.7))

ax.set_title("3D Bangladesh Shape")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_zlabel("Height")
ax.view_init(elev=30, azim=45)

plt.show()

