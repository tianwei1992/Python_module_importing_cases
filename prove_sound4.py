"""Wrong instance: import xx.xx.xx,the last one shouldn't be a function
"""
import sound.effects.echo.echo_effects
echo_effects()
"""
Result:
ModuleNotFoundError: No module named 'sound.effects.echo.echo_effects'; 'sound.effects.echo' is not a package"""