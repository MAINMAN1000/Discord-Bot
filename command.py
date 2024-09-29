import sqlite3
from discord.ext import commands

# This function will be called in Main.py to set up commands
def setup(bot):
    print("Setting up commands...")
    @bot.command()
    async def info(ctx, strain_name: str):
        # Connect to the SQLite database
        conn = sqlite3.connect('kushy.db')
        cursor = conn.cursor()

        # Query the database for the strain
        cursor.execute("SELECT * FROM strains WHERE name = ?", (strain_name,))
        strain_info = cursor.fetchone()

        # Check if strain exists
        if strain_info:
            await ctx.send(f"Strain: {strain_info[0]}\nType: {strain_info[1]}\nTHC Level: {strain_info[3]}\nCBD Level: {strain_info[4]}\nFlavor: {strain_info[5]}\nEffects: {strain_info[6]}\nMedical Uses: {strain_info[7]}")
        else:
            await ctx.send(f"No information found for strain: {strain_name}")

        # Close the connection
        conn.close()
