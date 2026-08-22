wall_area = float(input("Enter Area of one wall: "))
interior_cost = float(input("Enter cost of painting interior wall per unit area: "))
exterior_cost = float(input("Enter cost of painting exterior wall per unit area: "))

total_interior = wall_area * 4 * interior_cost
total_exterior = wall_area * 4 * exterior_cost
total = total_interior + total_exterior

print("Interior Painting Cost =", total_interior)
print("Exterior Painting Cost =", total_exterior)
print("Total Painting Cost =", total)
