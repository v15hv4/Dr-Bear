import { Navbar, NavbarBrand } from "reactstrap";

const Navigation = () => {
    return (
        <Navbar light className="custom-bg-primary mb-2">
            <NavbarBrand href="/" className="font-weight-bold custom-fg-primary">
                Dr Bear
            </NavbarBrand>
        </Navbar>
    );
};

export default Navigation;
